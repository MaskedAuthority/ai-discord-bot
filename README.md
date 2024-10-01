# ai-discord-bot

Welcome to **ai-discord-bot**, where you can run any AI model locally using LM Studio. Follow the steps below to set up and start the server:

## Getting Started

### Prerequisites

Make sure you have installed [LM Studio](https://lmstudio.com/download) on your machine. LM Studio allows you to easily run AI models of your choice.

### Installation

1. **Download LM Studio:**
   - Visit [LM Studio](https://lmstudio.com/download) and install the tool on your machine.
   
2. **Run an AI Model:**
   - Open LM Studio and load the AI model you wish to run.

3. **Start the Server:**
   - After setting up your model in LM Studio, go to the server directory in your terminal and run the following command:
     ```bash
     start server
     ```

4. **Configure API Key:**
   - Before running your code, make sure to add your OpenAI API key in your environment. You can set the key in your environment like this:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```

5. **Run Your Code:**
   - Now that your server is running, you can proceed to run your code:
     ```bash
     python your_code.py
     ```

## Additional Notes

- Ensure that the server is running before executing your script.
- Replace `your_api_key_here` with your actual OpenAI API key.
  
Feel free to raise any issues or contribute!
