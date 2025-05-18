import streamlit as st
from openai import OpenAI

# Configure your OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your actual key
)

st.set_page_config(page_title="Agent Type Chat", layout="centered")

st.title("🤖 LLM Chat: Agent Types")
user_input = st.text_input("Ask something about agents:")

if st.button("Submit") and user_input:
    with st.spinner("Getting response..."):
        try:
            completion = client.chat.completions.create(
                model="meta-llama/llama-3.3-8b-instruct:free",
                messages=[
                    {"role": "user", "content": user_input},
                ],
                max_tokens=500,
                extra_headers={
                    "HTTP-Referer": "http://localhost",  # or your deployed site if hosted
                },
            )

            if (
                completion and
                completion.choices and
                len(completion.choices) > 0 and
                completion.choices[0].message and
                completion.choices[0].message.content
            ):
                st.success("Response:")
                st.write(completion.choices[0].message.content)
            else:
                st.error("Error: Could not retrieve message content.")
                st.write("Full API response:", completion)

        except Exception as e:
            st.error(f"Exception: {str(e)}")
