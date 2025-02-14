# 💖 Ishtam AI - AI-Powered Love Message Generator  

Ishtam AI is a romantic message generator powered by AI! It lets you send love notes, schedule emails, get date ideas, and chat with AI to craft heartfelt messages.  

## Installation & Setup  

### Install the Package  
Install Ishtam AI from PyPI using:  
```
 pip install ishtam_ai 
```
Verify the installation to ensure it is set up correctly:  
```
 python -c "import ishtam_ai; print('Package installed successfully!')" 
```

### Install & Run Ollama (For AI Responses)  
Ollama is required for AI-generated love messages. Install Ollama using:  
```
 curl -fsSL https://ollama.com/install.sh | sh 
```
Start the Ollama server before launching the app:  
```
 ollama serve 
```

### Log into Streamlit  
Ensure you are logged into Streamlit for full functionality:  
```
 streamlit login 
```

### Set Up Email Credentials  
To send love emails, set up your email environment variables:  
```
 export EMAIL_ADDRESS="your-email@gmail.com" 
 export EMAIL_PASSWORD="your-app-password" 
```
Gmail users must generate an App Password from Google App Passwords instead of using their regular password. Check if they are set correctly:  
```
 echo $EMAIL_ADDRESS 
 echo $EMAIL_PASSWORD 
```

### Run the Streamlit App  
First, check where the application file is located using:  
```
 ls ishtam_ai/ 
```
If the application file is inside the Ishtam AI directory, use the appropriate command to run Streamlit:  
```
 streamlit run ishtam_ai/app.py 
```
If the application file is in the project root, use the corresponding command:  
```
 streamlit run app.py 
```

## Using the App  

Once the Streamlit app launches in your browser, you can:  
- Chat with AI to get personalized romantic messages  
- Send Love Emails to surprise your partner with heartfelt notes  
- Schedule Recurring Messages to automate love messages over time  
- Get Date Ideas with AI-powered date planning  

## Troubleshooting  

- If Ollama is not running, ensure it has been started:  
```
 ollama serve 
```
- If there is a Streamlit file error, use the correct command to run the application:  
```
 streamlit run ishtam_ai/app.py 
```
 or  
```
 streamlit run app.py 
```
- If emails are not sending, check the credentials:  
```
 echo $EMAIL_ADDRESS 
 echo $EMAIL_PASSWORD 
```
- Gmail users must set up an App Password from Google App Passwords.  

## Updating the Package  

To update Ishtam AI, change the version in the configuration file:  
```
 version = "1.0.1" 
```
Then, rebuild and upload the package:  
```
 python -m build 
 twine upload dist/* 
```

## License  

This project is licensed under the MIT License.  

## Enjoy Ishtam AI!  

Now you can spread love with AI-powered messages! Let me know if you need any help!

