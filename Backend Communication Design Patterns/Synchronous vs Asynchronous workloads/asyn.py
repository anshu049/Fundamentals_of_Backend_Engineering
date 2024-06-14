import asyncio
import aiofiles

async def main():
    # Print the first log message
    print("1\n")

    # Read the file asynchronously
    async with aiofiles.open("test.txt", "r") as file:
        res = await file.read()

    # Print the file contents with a newline after
    print(f"file: {res}\n")

    # Print the second log message
    print("2")

# Run the async main function
asyncio.run(main())

