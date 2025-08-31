from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name} agrega el comando /lista sesguido de los enlaces separados por un espacio')

async def lista_enlaces(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Recibe un comando /lista seguido de palabras separadas por espacios y
    envía cada palabra como un mensaje independiente al mismo chat.
    """
    # Obtiene el texto del mensaje completo
    texto_completo = update.message.text

    # Divide el texto en palabras, separando por espacios
    palabras = texto_completo.split()

    # Elimina el comando "/lista" de la lista de palabras
    if len(palabras) > 1:  # Verifica que haya algo después del comando
        palabras = palabras[1:]  # Slicing para obtener solo las palabras después del comando

        # Envía cada palabra como un mensaje independiente
        for palabra in palabras:
            try:
                await context.bot.send_message(chat_id=update.message.chat_id, text=palabra)
            except Exception as e:
                await context.bot.send_message(chat_id=update.message.chat_id, text=f"Error al enviar: {palabra} - {e}")
    else:
        await update.message.reply_text("Por favor, agrega palabras después del comando /lista.")


TOKEN = "8411105955:AAEIJSvG-eZPVB3e0jHZQSkfNlUP5tXG_eg"
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", say_hello))
application.add_handler(CommandHandler("lista", lista_enlaces))
application.run_polling(allowed_updates=Update.ALL_TYPES)
