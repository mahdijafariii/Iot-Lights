from langchain_openai import ChatOpenAI # pip install -U langchain_openai
class Ai:
    def handle_request(self,message):
        llm = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.avalai.ir/v1", api_key="aa-caTpQeo2t0FVA4tTJosaWwvwQcBsur8UpXugCoBbkizeA0NK")
        message = [
        {
        "role": "system",
        "content": """You are an assistant for an IoT system that
        controls LED lights. Based on the user's prompt, you must decide which
        function to call for controlling the lights.
        The function options are:
        A: turning on the light number 1,
        B: turning off the light number 1,
        C: turning on the light number 2,
        D: turning off the light number 2,
        E: turning on the light number 1 AND  turn off light number 2,
        F: turning on the light number 2 AND  turn off light number 1,
        You must only respond with a single character (A, B, C, D, E, or F)
        corresponding to the function. DO NOT add any other information or
        text.""",
        },
        {
        "role": "user",
        "content": message
        },
        ]
        result = llm.invoke(message)
        return(result.content)
