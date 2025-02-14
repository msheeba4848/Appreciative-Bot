# Ishtam AI - Custom AI-Powered Email Message Generator  

Ishtam AI is a custom AI-powered email generator! It allows users to send love notes, schedule emails, get date ideas, and chat with AI to create personalized messages tailored to their partner’s preferences.

## Installation & Setup  

### Setting Up a Virtual Environment  

It is recommended to install **Ishtam AI** in a virtual environment to avoid dependency conflicts.  

1. **Create a virtual environment**:  
   - On **Linux/macOS**:
   ```  
     python -m venv ishtam  
     source ishtam/bin/activate  
   ```
   - On **Windows (PowerShell)**:  
    ```
     python -m venv ishtam  
     ishtam\Scripts\Activate  
    ```

### Install the Package  

Install Ishtam AI from PyPI:  

```
pip install ishtam_ai  
```

Verify the installation:  

```
python -c "import ishtam_ai; print('Package installed successfully!')"
```  

---

## Running AI-Powered Features  

### Install & Run Ollama (For AI Responses)  

Ollama is required for AI-generated love messages.  

- On **Linux**:  
```
  curl -fsSL https://ollama.com/install.sh | sh  
```
- On **MacOS/Windows** (requires Homebrew):  
  If **Homebrew is not installed**, install it first:  
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"  
  ```

  Then, install Ollama:  
  ```
  brew install ollama  

  ```

Before running the app, **start the Ollama server**:  

```
ollama serve  
```

---

## Using Streamlit  

### Running the Streamlit App  

Before launching, check **where Ishtam AI is installed**:  
```
python -c "import ishtam_ai; print(ishtam_ai.__path__[0])"  
```

If installed inside a virtual environment or system-wide, run:  
```
streamlit run $(python -c "import ishtam_ai; print(ishtam_ai.__path__[0])")/app.py  
```

### Logging into Streamlit  

Streamlit login is optional, but if required:  
```
streamlit login  
```

---

## Setting Up Email Credentials  

To send emails, **configure email credentials** as environment variables:  

```
export EMAIL_ADDRESS="your-email@gmail.com"  
export EMAIL_PASSWORD="your-app-password"  
```

### Google App Passwords  
If using Gmail, **generate a 16-digit App Password** instead of using your actual password.  
To generate an **App Password**:  
1. Go to Google **Account Security Settings**  
2. Select **App Passwords**  
3. Generate a **16-character** password  
4. Use the generated password as `$EMAIL_PASSWORD`  

Verify that credentials are set:  
```
echo $EMAIL_ADDRESS  
echo $EMAIL_PASSWORD  
```

---

## Using the App  

Once the Streamlit app launches, you can:  
- **Chat with AI** for personalized romantic messages  
- **Send Love Emails** with heartfelt notes  
- **Schedule Recurring Messages** to automate love messages  
- **Get AI-Powered Date Ideas**  

---

## Upgrading the App

```
pip install --upgrade ishtam_ai

```

---

## Troubleshooting  

**Ollama Not Running?**  
Ensure the Ollama server is active:  
```
ollama serve  
```

**Streamlit File Error?**  
Use the correct command to run Streamlit:  
streamlit run ishtam_ai/app.py  

**Emails Not Sending?**  
Check email credentials:  
```
echo $EMAIL_ADDRESS  
echo $EMAIL_PASSWORD  
```

**Gmail Users:** Ensure App Passwords are set up correctly.  


## License  

This project is licensed under the **MIT License**.  

## Enjoy Ishtam AI!  

Now you can spread love with **AI-powered messages**! Let me know if you need any help.  
