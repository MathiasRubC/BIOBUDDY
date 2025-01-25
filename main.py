import discord
from discord.ext import commands
import os

# Configurar los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot con prefijo "!" y transferirle los privilegios
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Verificar si el mensaje es un comando válido
    ctx = await client.get_context(message)
    if ctx.valid:
        await client.process_commands(message)  # Procesar comandos válidos
    elif message.content.startswith('!'):
        # Responder para comandos desconocidos
        await message.channel.send("No puedo procesar este comando. Escribe `!ayuda` para ver los comandos disponibles.")

# Comando para mostrar ayuda
@client.command(name="ayuda")
async def ayuda(ctx):
    help_message = (
        "Hola, soy **BIOBUDDY** y te voy a ayudar en lo que necesites. Aquí están los comandos que puedes usar:\n\n"
        "`!informacion` - Explicación sobre qué es el medio ambiente y su importancia.\n"
        "`!reciclaje` - Consejos detallados para separar y manejar los residuos de forma ecológica.\n"
        "`!cuidado` - Recomendaciones para preservar el medio ambiente en tu vida diaria.\n"
        "`!ejemplos` - Ejemplos claros de acciones ecológicas que puedes implementar hoy.\n"
        "`!datos` - Datos curiosos y sorprendentes sobre el medio ambiente.\n"
        "`!impacto` - Información sobre el impacto de nuestras acciones en el medio ambiente.\n"
        "`!adios` - Despedida amigable de BIOBUDDY."
    )
    await ctx.send(help_message)

# Comando: información sobre el medio ambiente
@client.command()
async def informacion(ctx):
    info_message = (
        "El medio ambiente incluye todo lo que nos rodea: aire, agua, tierra, flora y fauna. Es el soporte "
        "de la vida en nuestro planeta. La contaminación, la deforestación y el cambio climático están poniendo "
        "en peligro este equilibrio, y por eso es crucial que tomemos acciones para protegerlo. 🌎\n\n"
        "**¿Sabías que?** Los ecosistemas saludables son esenciales para la supervivencia de todas las especies, "
        "incluidos los humanos."
    )
    image_path = "imagenes/informacion.jpg"
    await send_message_with_image(ctx, info_message, image_path)

# Comando: consejos sobre reciclaje
@client.command()
async def reciclaje(ctx):
    tips = (
        "**Reciclar ayuda a reducir la cantidad de desechos que terminan en los vertederos y los océanos.**\n\n"
        "Aquí tienes algunos consejos útiles:\n"
        "1. **Clasifica tus residuos:** Usa contenedores separados para plástico, papel, vidrio y orgánicos.\n"
        "2. **Limpia los materiales reciclables:** Los envases sucios pueden contaminar otros reciclables.\n"
        "3. **Evita plásticos de un solo uso:** Opta por bolsas reutilizables y envases retornables.\n"
        "4. **Reutiliza lo que puedas:** Dale una segunda vida a frascos, botellas y otros productos."
    )
    image_path = "imagenes/reciclaje.jpg"
    await send_message_with_image(ctx, tips, image_path)

# Comando: cuidado del medio ambiente
@client.command()
async def cuidado(ctx):
    consejos = (
        "**El cuidado del medio ambiente comienza con pequeñas acciones en tu día a día.**\n\n"
        "1. **Ahorra energía:** Apaga luces y desconecta dispositivos cuando no los uses.\n"
        "2. **Usa transporte sostenible:** Camina, usa bicicleta o transporte público para reducir emisiones.\n"
        "3. **Protege la biodiversidad:** Planta árboles y cuida de los espacios verdes en tu comunidad.\n"
        "4. **Reduce el consumo de agua:** Cierra el grifo mientras te cepillas los dientes o lavas platos.\n"
        "5. **Consume de forma responsable:** Apoya productos locales y evita comprar cosas que no necesitas."
    )
    image_path = "imagenes/cuidado.jpg"
    await send_message_with_image(ctx, consejos, image_path)

# Comando: ejemplos de acciones ecológicas
@client.command()
async def ejemplos(ctx):
    ejemplos = (
        "**Tomar acción por el medio ambiente no tiene que ser complicado. Aquí tienes algunos ejemplos fáciles:**\n\n"
        "1. Usa botellas reutilizables para evitar el plástico desechable.\n"
        "2. Lleva tus propias bolsas de tela cuando vayas de compras.\n"
        "3. Crea un huerto casero con hierbas o vegetales en macetas.\n"
        "4. Participa en jornadas de limpieza de playas, parques o calles.\n"
        "5. Comparte con tu comunidad formas de cuidar el medio ambiente."
    )
    image_path = "imagenes/ejemplos.jpg"
    await send_message_with_image(ctx, ejemplos, image_path)

# Comando: datos curiosos sobre el medio ambiente
@client.command()
async def datos(ctx):
    datos_curiosos = (
        "**Descubre algunos datos sorprendentes sobre el medio ambiente:**\n\n"
        "1. **Un solo árbol puede absorber hasta 21 kilos de dióxido de carbono por año.**\n"
        "2. El reciclaje de una sola botella de vidrio ahorra suficiente energía para encender un foco durante 4 horas.\n"
        "3. Los océanos producen más del 50% del oxígeno del planeta.\n"
        "4. **Cada minuto se tira suficiente plástico para llenar un camión de basura.**\n"
        "5. Más del 70% de los cultivos alimentarios dependen de la polinización de las abejas."
    )
    image_path = "imagenes/datos.png"
    await send_message_with_image(ctx, datos_curiosos, image_path)

# Comando: impacto de nuestras acciones en el medio ambiente
@client.command()
async def impacto(ctx):
    impacto_info = (
        "**Nuestras acciones tienen un impacto directo en el medio ambiente.**\n\n"
        "1. El uso excesivo de combustibles fósiles contribuye al cambio climático.\n"
        "2. La tala indiscriminada de árboles afecta a la biodiversidad y aumenta el dióxido de carbono en el aire.\n"
        "3. El consumo excesivo de productos plásticos causa contaminación en los océanos.\n"
        "4. Las emisiones de gases de efecto invernadero aceleran el calentamiento global.\n"
        "5. El desperdicio de agua afecta a las reservas hídricas del planeta.\n\n"
        "**¿Sabías que?** Si reducimos el consumo de recursos y adoptamos hábitos sostenibles, podemos disminuir nuestro impacto negativo y ayudar a proteger el planeta."
    )
    image_path = "imagenes/impacto.jpg"
    await send_message_with_image(ctx, impacto_info, image_path)

# Comando: despedida
@client.command(name="adios")
async def adios(ctx):
    despedida_message = (
        "Espero haberte ayudado con esta guía para el medio ambiente. 🌿\n"
        "**Recuerda que solo tenemos un planeta. ¡Cuidémoslo juntos!** 🌍"
    )
    await ctx.send(despedida_message)

# Función auxiliar para enviar un mensaje con una imagen
async def send_message_with_image(ctx, message_text, image_path):
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(message_text, file=picture)
    else:
        await ctx.send(message_text + "\n⚠️ No se encontró la imagen asociada.")

# Ejecutar el bot con tu token
client.run('TOKEN')

