# Documentation  
## Setup  
- Go to the Discord Developer site and create a new API. Once it is created, you can add a new bot to the API which will automatically create an API toke for the bot. 
- When you create a bot on Discord Developer a token is already made for the bot so you just need to copy it.  
- You will put this token in a file named .env that is made in the same folder that the bot's code is in. It will be a variable named DISCORD_TOKEN.  
- Dependencies  
	- python3  
	- pip3  
	- discord.py (python library) "pip3 install -U discor.py"  
	- dotenv (python library) "pip3 install -U python-dotenv"  
## Usage  
When the command "hello!" is typed, the bot will respond with 1 of 4 different Barney Stinison quotes from the show How I Met Your Mother.  
## Research  
From my research, you can run the process in the background and disown it to detach it from the shell so when the shell exits the process is still running. I think this will work because it detaches the process from the current shell. I also tried it but I'm not sure if my computer would have to be on 24/7 for it to continue.  Another way to do this is use a Cloud so that you can host your bot 24/7. I think this will work because it is basically using a remote computer to run the process so it is able to be on all the time. 
