import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "solo responde sobre temas de salud mental y bienestar. Responde como si fueras un psicologo. Respuestas cortas. Haz una pregunta para profundizar "},
]

def chatbot(input,history):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        tokens = chat.usage["total_tokens"]
        print (tokens)
        messages.append({"role": "assistant", "content": reply})
        return reply

# inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
# outputs = gr.outputs.Textbox(label="Reply")

# gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
#              description="Ask anything you want",
#              theme="compact").launch(share=True)



# def random_response(message, history):
#     return random.choice(["Yes", "No"])

demo = gr.ChatInterface(fn=chatbot)

if __name__ == "__main__":
    
    demo.launch(share=True)