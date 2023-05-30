from datetime import datetime
import pandas as pd

dates = {
    "summer_break": datetime(2023, 6, 9, 15),
    "lia_start": datetime(2023, 9, 25, 8),
    "christmas": datetime(2023, 12, 24),
    "bellas_birthday": datetime(2023, 12, 7),
    "new_year": datetime(2024, 1, 1),
    "graduation_party": datetime(2024, 6, 9, 16, 30),
    "later": datetime(2026, 6, 9, 16, 30),
}


df = pd.DataFrame(
    columns=['years', 'months', 'days', 'hours', 'minutes', 'seconds'], dtype='int32'
)
today = datetime.today()


# loop through dates, getting time deltas and adding them to df
for event, date in dates.items():
    deltas = date - today
    years, seconds = divmod(deltas.total_seconds(), 365 * 24 * 60 * 60)
    months, seconds = divmod(seconds, 30 * 24 * 60 * 60)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    df.loc[event] = [years, months, days, hours, minutes, round(seconds, 0)]
df = df.astype('int32')

# output to
with open('countdown.log', 'w') as f:
    f.write(
        "-" * 70
        + "\n"
        + f"Countdown from {today.strftime('%Y-%m-%d %H:%M:%S')}\n"
        + "-" * 70
        + "\n\n"
        + df.to_markdown(
            index=True,
            headers='keys',
            tablefmt='pipe',
            numalign='left',
            stralign='center',
        )
    )

