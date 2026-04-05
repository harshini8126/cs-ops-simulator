import gradio as gr
from inference import run_task, get_action_from_llm

def run_simulation(task):
    return run_task(task)

def test_single_email(subject, body):
    class Email:
        def __init__(self, subject, body):
            self.subject = subject
            self.body = body

    email = Email(subject, body)
    result = get_action_from_llm(email)

    return str(result)

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 CSOps Agent Simulator")

    with gr.Tab("Run Task Simulation"):
        task_input = gr.Dropdown(
            choices=["easy", "medium", "hard"],
            label="Select Task"
        )
        task_output = gr.Textbox(lines=15, label="Output")
        run_btn = gr.Button("Run Simulation")

        run_btn.click(run_simulation, inputs=task_input, outputs=task_output)

    with gr.Tab("Test Single Email"):
        subject_input = gr.Textbox(label="Email Subject")
        body_input = gr.Textbox(label="Email Body", lines=5)

        single_output = gr.Textbox(label="Prediction")

        test_btn = gr.Button("Classify Email")

        test_btn.click(test_single_email, inputs=[subject_input, body_input], outputs=single_output)

demo.launch(server_name="0.0.0.0", server_port=7860)
