### RUX - LLM Companion Backend 

## Project Overview :
- This is a Backend LLM - companion made by using FAST-API , has a local memory (used for prototyping) and is integrated with a Local LM via LM studio (model-Qwen v3 4B). 

## GOAL :
- My goal with this project is to bulid while learning how LLM is being develop and how it can be integrated in an app.

## Features : 
- The features this project provide could be classified as follows : 

- 1. Rule-Based Logic : I have used this logic for it's determinism and reliability which can be consider better than LLMs.

- 2. Memory : I have included a local memory state for the LLM to access , I have used this for remembering the name provided by the user and to greet , this makes the prototype to be more alive.

- 3. LLM fall back : This helps in redirecting the requests from the user to the LM if Rule-Based Logic fails , this helps in accessing the Local LM (Qwen v3 4B).

## System Architecture : 
- The system architecture could be mapped as follows :

- User -> Fast-API (/chat) -> Rule-Based Logic (Deterministic) -> In-Memory Management (User context) -> LLM Fallback (Local via LM studio) -> Response .

## Tech Stack :
- Here is an overview on what tech stack i have been using currently :

# Core Language :
- **Python** - used for all the backend logic , memory handling and LLM integration.

# Backend Framework :
- **FAST-API** - I have used this framework for its fast request/reponse handling and clean Swagger UI .

# Data Validation :
- **Pydantic** - This python libary is very useful for it's Input Schema(Chatrequest) , type safety and clean parsing.

# LLM / LLM Intergration :
- Local Large Model (LLM) via LM studio | Model - Qwen 3 (4B Instruct) :
- I have used this model as its locally and *freely* available. 

# HTTP Client :
- **Requests**









