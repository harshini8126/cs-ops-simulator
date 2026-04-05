import gradio as gr
from inference import run_task, get_action_from_llm
from models import Action

def run_simulation(task):
    return run_task(task)

def test_single_email(subject, body):
    class Email:
        def __init__(self, subject, body):
            self.id = "custom_1"
            self.subject = subject
            self.body = body

    email = Email(subject, body)
    result = get_action_from_llm(email)
    return str(result)

def run_custom_email(subject, body):
    class Email:
        def __init__(self, subject, body):
            self.id = "custom_1"
            self.subject = subject
            self.body = body

    email = Email(subject, body)
    data = get_action_from_llm(email)

    action = Action(
        email_id=email.id,
        category=data["category"],
        priority=data["priority"],
        decision=data["decision"],
        reply=data["reply"]
    )

    return action.dict()

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 CSOps Agent Simulator")
    gr.Markdown("Simulates a customer support agent using an OpenEnv-style environment.")

    with gr.Tab("Run Task Simulation"):
        task_input = gr.Dropdown(choices=["easy", "medium", "hard"], label="Select Task")
        task_output = gr.Textbox(lines=20, label="Simulation Output")
        run_btn = gr.Button("Run Simulation")
        run_btn.click(run_simulation, inputs=task_input, outputs=task_output)

    with gr.Tab("Test Single Email"):
        subject_input = gr.Textbox(label="Email Subject")
        body_input = gr.Textbox(label="Email Body", lines=5)
        single_output = gr.Textbox(label="Prediction")
        test_btn = gr.Button("Classify Email")
        test_btn.click(test_single_email, inputs=[subject_input, body_input], outputs=single_output)

    with gr.Tab("Custom Email Simulation"):
        subject_input2 = gr.Textbox(label="Email Subject")
        body_input2 = gr.Textbox(label="Email Body", lines=5)
        action_output = gr.JSON(label="Agent Action Output")
        run_btn2 = gr.Button("Run Agent")
        run_btn2.click(run_custom_email, inputs=[subject_input2, body_input2], outputs=action_output)

demo.launch(server_name="0.0.0.0", server_port=7860)
