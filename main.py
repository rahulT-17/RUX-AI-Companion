from fastapi import FastAPI
from pydantic import BaseModel
## IMPORTING OPEN AI
import os 
from openai import OpenAI

## APP CONFIGURATION :
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI(
    title="RUX AI",
    description="Backend for a voice-based AI companion with memory",
    version="1.0"
)

# APP'S MEMORY (STATE)
# FOR : SINGLE USER , IN-MEMORY ,RESETS ON SERVER RESTART, FOR PROTOTYPING
memory = {
    "name": None ,
    
}

## Request Model : defines what data the client (app) must send 

class ChatRequest(BaseModel):
    '''
    DEFINES STRUCTURE OF THE INCOMING CHAT WITH THE USER
    '''
    message: str

 
## helper function : for extracting name from user input :
def extract_name(message: str) -> str :
    '''
    Extract and format user name from the input
    ex : my name is rahul == 'Rahul'
    '''
    return message[len("my name is"):].strip(" .?!,").title()

## LLM integrated

def llm_reply(user_message: str, memory: dict ) -> str:
    """
    Generates a converstional reply using LLM.
    memory is passed as context but not modified.
    """
    system_prompt = f"""
                You are RUX, a friendly AI companion.
                The user's name is : {memory.get("name")}.
            If the name is None , do not guess it.
            Be cool , supportive ,casual and clear.
            """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content.strip()

# ROOT ENDPOINT : creates the main http :~
@app.get("/")
def root():
    '''
    Used for verify the backend is working 
    '''
    return {"message": "AI Companion Backend is running"}

## chat endpoint : 
@app.post("/chat")
def chat(request: ChatRequest):

    # input for reliable matching :
    user_message = request.message.lower().strip()
     
    # used for debugging can be removed later.
    print("RAW MESSAGE:", repr(request.message))
    print("NORMALIZED:", repr(user_message))


    ## RULED BASED THINKING :
    # 1. checking if user tells his name : USER INTRODUCES NAME (STRICT MATCH) ? 
    if user_message.startswith("my name is"): 
        name = extract_name(user_message)
        memory["name"] = name
        reply = f"What's up, {name}"

    # 2. checking if user asks for his name :
    elif user_message in ["what is my name", "what's my name"] :
        if memory["name"] :
            reply = f"I remember you {memory['name']}"
        else:
            reply = "I dont recall."
        
    # 3. greeting
    elif user_message in ["hi", "hello", "hey"] :
        reply = "Hey!! what's up, how may i assist you today."
    
    # 4. asking your my name :
    elif "who are you" in user_message :
        reply = "I'm RUX an AI companion. I'll be around if you need me"
    
    # help box
    elif "help" in user_message :
        reply = "Umm , Tell me what's bothering you"
    
    ## fall back :
    else :
        reply = llm_reply(request.message, memory)
        
    return {
        "reply" : reply
    }


