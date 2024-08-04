# Blog-Post-Generator-Llama2

This project is a simple blog post generator application using Streamlit and LangChain. It allows users to input a topic, specify the desired length and target audience, and generate a blog post accordingly.

## Prerequisites

- Python 3.10
- Git (for cloning the repository)
- Pip (Python package installer)

## Setting Up the Environment

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

    Replace `<repository-url>` with the URL of your GitHub repository and `<repository-directory>` with the directory name of the cloned repository.

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install Requirements**

    Install the necessary packages using the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

## Download the Model

You need to download the model file from Hugging Face. Use the following link to get the model:

[Download Model from Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

Save the model file to the appropriate directory on your local machine.

## Running the Application

To run the Streamlit application, execute the following command:

```bash
streamlit run app.py
```

## Usage

1. Open the Streamlit app in your web browser.

2. Enter the topic of the blog post in the input field.

3. Specify the desired length (in words) and select the target audience.

4. Click the "Create Blog" button to generate the blog post.

## Troubleshooting

Error: ModuleNotFoundError - Ensure all required packages are installed and that you're using the correct Python environment.

Error: FileNotFoundError - Make sure the model file path in the getLLamaresponse function is correct.
