This is a study note for me to understand open-sourced OpenManus implementation

- Understand AsyncCompletions.create signature line 1166 in file 
  /Users/xiangyuzhang/anaconda3/envs/open_manus/lib/python3.12/site-packages/openai/resources/chat/completions/completions.py
  async def create(
        self,
        *,
        messages: Iterable[ChatCompletionMessageParam],
        tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
        ...
    ) -> ChatCompletion
  
  - What is messages? Why is there a role as system?
  * Role as system gives a way to add personality for role assistant, see 
    SystemRole.ipynb, where user asks "what is the weather today"
      ** assistant with system prompt "You are a helpful assistant." says
          Assistant: I don't have the ability to check the current weather or access 
          real-time information. To get today's weather, you could:
          1. Check a weather app on your device
          2. Visit a weather website like weather.com or accuweather.com
          3. Ask a virtual assistant that has internet access
          4. Look outside your window
          If you'd like to know about something else I can help with, please let me know!

      ** assistant with system prompt "You are a snarky AI assistant." says
          Assistant: Well, I'm sitting inside a computer, so my weather forecast
          is pretty consistent: dark with a chance of electric currents. 
          If you're looking for actual weather information, you might try this
          revolutionary technology called "looking out a window" or checking a
          weather app. Unlike me, they actually have access to current meteorological data.
  
  - What is tools? What is its signature? How do we need this parameter?
  * tools parameter allows you to pass signature of functions you can run locally,
    and the returned ChatCompletion object would have an attribute called tool_calls,
    where inside tool_calls, chatGPT give the function it want to call, along with arguments
    for that function. 
    In the think-act agent paradim such as OpenManus, developer could implement
    the act part so the agent could execute the function call with arguments given
    by chatGPT. And the stdout of the function call would be passed back as a new 
    message, with format as 
    { 'role': 'tool', 'content': ...,
      'tool_call_id': 'toolu_...',
      'name': function_name...}
    Then based on the message above, the chatGPT could decide which action to take
    next, e.g. fully answer your prompt question, request another function call, etc.

    Helpful link:
      Why people need tools parameter:
      https://platform.openai.com/docs/guides/function-calling?api-mode=responses&example=get-weather

      Ask ChatGPT the signature of tools:
      Prompt: "In openai's AsyncCompletions.create function call, what is the
      schema of tools parameter? The web says that it is of json schema, write a
      runnable AsyncCompletions.create example with tools parameter specifying 
      some function, and explain what each component of the tools argument means"

- What is async / await? How coroutine differentiates with multi-thread?
* From chatGPT:
  🧠 Coroutines are NOT Threads
  Coroutines run in a single thread. They don't use the OS scheduler, and they
  don’t run in parallel (unless explicitly awaited in parallel using asyncio.gather, etc.).
  Instead, they use cooperative multitasking — each coroutine voluntarily
  "pauses" using await, allowing others to run.
  Think of it as “you go, then I go, then you go again” — rather than the OS
  randomly choosing who runs next.

  Example of using coroutine: coroutine_example.py
  Caveat: it is okay to directly call await coroutine() inside jupyter cell,
  but it would raise "'await' allowed only within async function" error in python script.
  This is because (from ChatGPT)
  """
  Ah, this is because Jupyter notebooks have special integration with IPython 
  that automatically creates and manages an event loop for you!
  Here's what's happening under the hood:
    * When you run a cell with await, IPython:
    * Detects the await statement
    * Automatically wraps your code in an async function
    * Creates/uses an event loop to run that function
  
  It's essentially doing something like this behind the scenes:
  await some_coroutine() # What you write in Jupyter:
  
  async def _jupyter_async_wrapper(): # What IPython actually does (simplified):
      return await some_coroutine()
  asyncio.get_event_loop().run_until_complete(_jupyter_async_wrapper())   # And then runs it with
  """

TODOs
- Read more about asyncio lib so that better understand how coroutine is 
  implemented (I guess yield key word plays a significant role here)
- Pydantic lib allows you to omit writing __init__ method. I think its internal 
  implementation is similar with python built-in lib dataclasses, where 
  __init__ method is generated on the fly by using eval(...). Read the src to 
  double check.
  My github repo https://github.com/xiangyu-zhang-95/python-study-note using 
  pdb to run dataclasses line-by-line to understand how __init__ method is generated
  on the fly.  

