import asyncio
from playwright.async_api import async_playwright

# chat popout link
CHAT_URL = "https://www.youtube.com/live_chat?is_popout=YOUR_LINK"

async def main():
    async with async_playwright() as p:
        print("Parsing connection to excisting Chrome (port 9223)...")
        try:
            browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9223")
        except Exception as e:
            print(f"Connection error: {e}")
            return

        context = browser.contexts[0]
        page = context.pages[0] if context.pages else await context.new_page()
        
        print(f"Opening chat...")
        await page.goto(CHAT_URL)
        
        # giving it some time to avoid errors
        await asyncio.sleep(10)
        
        # selector to start typing
        chat_input_selector = "yt-live-chat-text-input-field-renderer div#input"

        k = 1
        slowmodeSleep = 20  # customize according to Slow Mode settings of each stream
        while True:
            for i in range(3):
                message = f"Message №{k+i}"  # feel free to customize it
                print(f"[{k+i}] Sendnig: {message}")
                
                try:
                    # clicking the typing window
                    chat_input = page.locator(chat_input_selector)
                    await chat_input.click()
                    
                    # Ctrl+A -> Backspace
                    await page.keyboard.press("Control+A")
                    await page.keyboard.press("Backspace")
                    
                    # human immitation🤓
                    await page.keyboard.type(message, delay=80)
                    await asyncio.sleep(0.5)
                    
                    await page.keyboard.press("Enter")
                    print(f"Message sent. Waiting {slowmodeSleep} seconds...")  
                    
                except Exception as e:
                    print(f"Error while trying to send: {e}")
                
                await asyncio.sleep(slowmodeSleep)
            
            k += 3
            print(f"--- Executed. Waiting for the next xp drop ---")
            await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
