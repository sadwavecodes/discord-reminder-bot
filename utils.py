from reminders import reminder, cancelreminder
from help import setup_help

def setup_bot(bot):
    @bot.command(name='reminder', help='Set a reminder. Usage: !reminder <time> <message>\nTime examples: 1s, 1m, 1h, 1d')
    async def reminder_command(ctx, time: str, *, reminder_text: str):
        await reminder(ctx, time, reminder_text=reminder_text)

    @bot.command(name='cancelreminder', help='Cancel a reminder by ID. Usage: !cancelreminder <reminder_id>')
    async def cancelreminder_command(ctx, reminder_id: int):
        await cancelreminder(ctx, reminder_id)

    # Set up help command
    setup_help(bot)