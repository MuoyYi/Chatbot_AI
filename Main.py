from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Define your bot token and username
TOKEN: Final = '7553056247:AAENtw8B88VaR7LzUn_ssMtT4NgIaw_l4JI'
BOT_USERNAME: Final = '@Geological_Dictionary_bot'

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a Geological dictionary!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Geological dictionary! Please type something so I can respond.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Response handler function
def handle_response(text: str) -> str:
    processed: str = text.lower()  # Convert to lowercase for consistent matching
    
    # Match known geological terms with their responses
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    if 'mineral' in processed:
        return 'A naturally occurring, solid substance with a specific chemical composition and structure.' 
    if 'sediment' in processed:
        return 'Particles of rock, minerals, or organic material deposited by water, wind, or ice.'
    if 'erosion' in processed:
        return 'The process of wearing away rocks and soil by natural forces like water and wind.' 
    if 'fossil' in processed:
        return 'Preserved remains or impressions of ancient organisms found in rock.'
    if 'weathering' in processed:
        return 'The breakdown of rocks into smaller particles by chemical, physical, or biological processes.'
    if 'xenolith' in processed:
        return '-	Xenolith means a fragment of rock that is embedded in another rock. The term is most often used in geology to describe rock fragments that become trapped in igneous rock during its development and solidification.'
    if 'xenolite' in processed:
        return 'XENOLITE is a lead-free, super-lightweight, flexible and recyclable x-radiation protection material.'
    if 'xenotime' in processed:
        return 'Xenotime is a yttrium phosphate mineral with high rare earth oxide content.'
    if 'ore' in processed:
        return 'A natural mineral deposit that can be mined profitably for metals or other valuable elements.'
    if 'mineral deposit' in processed:
        return 'A naturally occurring concentration of minerals, valuable for economic extraction.'
    if 'resource' in processed:
        return 'A total amount of a geologic material, like minerals or fossil fuels, in a given area.'
    if 'reserve' in processed:
        return 'The portion of a resource that is economically viable for extraction with current technology and prices.'
    if 'grade' in processed:
        return 'The concentration of a mineral within an ore, which affects its economic value.'
    if 'exploration' in processed:
        return 'The process of searching for economically viable mineral deposits through fieldwork, sampling, and drilling.'
    if 'mining' in processed:
        return 'The extraction of valuable minerals or other geological materials from the Earth.'
    if 'metallurgy' in processed:
        return 'The science of extracting metals from their ores and refining them for practical use.'
    if 'hydrothermal deposit' in processed:
        return 'A mineral deposit formed by hot, mineral-rich fluids moving through fractures in rocks.'
    
    # Default response if no known term is matched
    return 'I do not understand what you wrote...'



# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text  # Correct the text variable to get actual message text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Check if the message is in a group and bot is mentioned
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else: 
            return
    else: 
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Main function to start the bot
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message handler for text messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
