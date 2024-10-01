# ai-discord-bot

Welcome to **ai-discord-bot**, where you can run any AI model locally using LM Studio and create your own Discord bot. Follow the steps below to set up and start the server, and create your Discord bot.

## Getting Started

### Prerequisites

Make sure you have installed [LM Studio](https://lmstudio.ai/) on your machine. LM Studio allows you to easily run AI models of your choice.

### Installation

1. **Download LM Studio:**
   - Visit [LM Studio](https://lmstudio.ai/) and install the tool on your machine.
   
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
     ai = OpenAI(api_key="your open ai key")
     ```

5. **Run Your Code:**
   - Now that your server is running, you can proceed to run your code:
     ```bash
     python discord_bot.py
     ```

### Creating a Discord Bot

1. **Get a Discord Developer Account:**
   - Visit the [Discord Developer Portal](https://discord.com/developers/docs/intro) and log in with your Discord account.

2. **Create a New Application:**
   - Click on **New Application** and give your bot a name. Choose all the necessary settings for your Discord bot, such as name, avatar, and description.

3. **Configure OAuth2 for Your Bot:**
   - Go to the **OAuth2** tab in your application.
   - Under the OAuth2 settings, select **bot** and any other permissions your bot will need.
   - Copy the generated OAuth2 URL and use it to invite the bot to your Discord server.

4. **Invite the Bot:**
   - Paste the OAuth2 URL in your browser and follow the steps to invite the bot to your Discord server.

## Additional Notes

- Ensure that the server is running before executing your script.
- Replace `your_api_key_here` with your actual OpenAI API key.
- After configuring the Discord bot, it should be visible in the server where it was invited.

Feel free to raise any issues or contribute!
