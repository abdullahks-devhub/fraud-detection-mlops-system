import gradio as gr
import random
from src.pipeline.prediction_pipeline import PredictionPipeline

# Initialize the pipeline
pipeline = PredictionPipeline()

css = """
body {
    background-color: #0b0f19;
    color: #e2e8f0;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
}
.gradio-container {
    background-color: transparent !important;
}
.card {
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    backdrop-filter: blur(10px);
}
.title-text {
    font-size: 2.5em;
    font-weight: 800;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
.predict-btn {
    background: linear-gradient(90deg, #10b981, #059669) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.1em !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
.predict-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.4) !important;
}
.result-box {
    text-align: center;
    padding: 20px;
    border-radius: 12px;
    background: #1e293b;
    border: 1px solid #475569;
    margin-top: 20px;
}
.metric-value {
    font-size: 1.5em;
    font-weight: 700;
    margin-top: 5px;
}
"""

def generate_random():
    return [
        random.uniform(0, 100000),  # Time
        *[random.uniform(-3, 3) for _ in range(28)], # V1-V28
        random.uniform(1, 1000)  # Amount
    ]

def predict(*args):
    keys = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
    data = dict(zip(keys, args))
    
    result = pipeline.predict_with_risk(data)
    
    risk = result["risk_level"]
    prob = f"{result['fraud_probability'] * 100:.2f}%"
    conf = result["confidence"]
    
    color = "#10b981" if "LOW" in risk else "#f59e0b" if "MEDIUM" in risk else "#ef4444"
    
    html_output = f"""
    <div class="result-box" style="border-top: 4px solid {color};">
        <h3 style="color: #94a3b8; margin:0;">Fraud Assessment</h3>
        <div class="metric-value" style="color: {color}; font-size: 2em; margin: 10px 0;">{risk}</div>
        
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div>
                <div style="color: #64748b; font-size: 0.9em; text-transform: uppercase;">Probability</div>
                <div class="metric-value" style="color: #e2e8f0;">{prob}</div>
            </div>
            <div>
                <div style="color: #64748b; font-size: 0.9em; text-transform: uppercase;">Confidence</div>
                <div class="metric-value" style="color: #e2e8f0;">{conf}</div>
            </div>
        </div>
    </div>
    """
    return html_output

with gr.Blocks(css=css, theme=gr.themes.Monochrome()) as demo:
    gr.HTML("<h1 class='title-text'>Fraud Detection MLOps System</h1>")
    gr.HTML("<p class='subtitle'>Real-time inference dashboard powered by Scikit-Learn & Gradio</p>")
    
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Accordion("Transaction Details", open=True):
                time_in = gr.Number(label="Time (seconds elapsed)", value=0)
                amount_in = gr.Number(label="Transaction Amount ($)", value=150.0)
                
            with gr.Accordion("PCA Features (V1 - V28)", open=False):
                v_inputs = [gr.Number(label=f"V{i}", value=0.0) for i in range(1, 29)]
                
            with gr.Row():
                random_btn = gr.Button("🎲 Generate Random Transaction")
                predict_btn = gr.Button("🔍 Analyze Transaction", elem_classes="predict-btn")
                
        with gr.Column(scale=1):
            output_html = gr.HTML(value='<div class="result-box" style="color:#64748b;">Awaiting transaction...</div>')
    
    all_inputs = [time_in] + v_inputs + [amount_in]
    
    random_btn.click(fn=generate_random, outputs=all_inputs)
    predict_btn.click(fn=predict, inputs=all_inputs, outputs=output_html)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
