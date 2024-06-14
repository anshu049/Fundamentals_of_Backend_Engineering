import asyncio
import aiofiles

async def read_file_async(file_path):
    async with aiofiles.open(file_path, 'r') as file:
        return await file.read()

async def main():
    # Print the first log message
    print("1\n")

    # Read the file asynchronously
    file_content = await read_file_async("test.txt")

    # Print the second log message
    print("2\n")

    # Print the file contents with a newline after
    print(f"file: {file_content}\n")

# Run the main function
asyncio.run(main())
