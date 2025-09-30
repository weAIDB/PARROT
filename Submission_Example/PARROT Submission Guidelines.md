## PARROT Submission Guidelines

Thank you for participating in the PARROT Challenge! To ensure a fair, impartial, and efficient assessment, **all submissions are evaluated centrally by the PARROT Challenge organizers.**You are required to submit a complete, runnable code package, which we will evaluate on a hidden test set in an isolated environment. Your code and models will be kept strictly confidential.

To protect our test data, all submitted code will be reviewed carefully. **Please do not include any private API packages that could upload our data to external services.** Additionally, please ensure your submission package is concise, containing only the core files related to your work. Removing irrelevant files will help us conduct a faster and smoother evaluation. Thank you!

### 1. Submission Checklist

Please organize all the following files into a single root folder and compress it into a `.zip` archive.

**Example Folder Structure:**

```basic
20250928_MyTranslator_MyTeam/
├── README.md
├── metadata.yaml
├── code/
│   ├── run_translation.sh
│   └── ... (all your source code)
├── requirements.txt
```

- **`README.md` (Crucial):**

  - This is the **sole guide** we will follow to run your code. Please provide clear, copy-paste-ready instructions.
  - Must include:
    1. **Environment Setup Steps:** Besides `requirements.txt`, any special dependencies (e.g., packages installed via `apt-get`, specific Java versions, etc.) must be specified here.  **Our cuda version is**
    2. **Model Download Instructions:** How to download your model weights from Hugging Face or other cloud storage. Please ensure we have the necessary access permissions.
    3. ***Resource and Time Requirements:*** Please specify the resources required for inference (e.g., `1 x A100 80G`) ***and the approximate runtime on the development set (e.g., "approx. 2 hours"). This is mandatory for our planning.***
    4. ***Execution Command: The exact, single command to run the entire inference process. We require this to be encapsulated in the* `run_translation.sh` *script for one-click execution.***

- **`metadata.yaml` (Required):**

  - A structured file for displaying information about your method on the leaderboard.

  - Template:

    ```yaml
    # Your model's name (as it will appear on the leaderboard)
    model_name: "MyTranslator-Llama3-70B"
    # Your team or author name
    team_or_author: "MyTeam"
    # Base Large Language Model (if applicable)
    base_llm: "Llama-3-70B"
    # Model size in billions of parameters
    model_size: 70B
    ```

### 2. Core Execution Requirements: The Entrypoint Script

**Your `code/run_translation.sh` script is the single entrypoint for our automated evaluation and must run the entire process with one command, requiring only the input and output file paths as arguments. Submissions that need complex setup or multiple manual steps will not be evaluated.**

- **Invocation:**

  ```bash
  bash code/run_translation.sh /path/to/input.json /path/to/output.json
  ```

- **Input File (`input.json`) Format:**
   A JSON list, where each object represents an independent `source_dialect -> target_dialect` translation task.

  ```json
  [
    {
      "id": "parrot_task_001",
      "source_dialect": "PostgreSQL",
      "source_sql": "SELECT TO_TIMESTAMP(virtual_T1.\"day\" || '', 'YYYYMMDD')",
      "target_dialect": "ClickHouse"
    }
  ]
  ```

- **Output File (`output.json`) Format:**
   Your script must generate a JSON list. **Each output object should include the key fields from the input** and be appended with your translation result, creating a complete, self-contained record.

  ```json
  [
    {
      "id": "parrot_task_001",
      "source_dialect": "PostgreSQL",
      "source_sql": "SELECT TO_TIMESTAMP(virtual_T1.\"day\" || '', 'YYYYMMDD')",
      "target_dialect": "ClickHouse",
      "translated_sql": "SELECT formatDateTime(parseDateTimeBestEffort(toString(virtual_T1.day)), '%Y-%m-%d %H:%i:%s')"
    }
  ]
  ```

### 3. Packaging and Submission

1. **Packaging:** Compress the root folder containing all the above files into a single `.zip` archive. 
2. The final `.zip` file **must** be named according to the following format:
    `YYYYMMDD_ModelName_TeamName.zip`

   - **`YYYYMMDD`**: The date of your submission (e.g., `20250928`).
   - **`ModelName`**: Your model's name, which must match the `model_name` in your `metadata.yaml`.
   - **`TeamName`**: Your team or author name, which must match the `team_or_author` in your `metadata.yaml`.

   **Example:**
    If your `model_name` is "LLMTranslator" and your `team_or_author` is "ExampleTeam", and you are submitting on September 28, 2025, your final submission file should be named exactly as follows:

   `20250928_LLMTranslator_ExampleTeam.zip`
   
   This file is what you will upload for evaluation.

3. **Email Submission:**
   
   - **Recipient:** **[weizhoudb@sjtu.edu.cn](mailto:weizhoudb@sjtu.edu.cn)**
   - **Subject:** `[PARROT Submission] [Your_Model_Name] - [Your_Team_Name]`
   - **Body:**
     - A brief introduction to your method.
     - **If using a closed-source API (e.g., OpenAI):** Please provide your API key in the body of the email and inform us of the approximate token consumption on the dev set. We will notify you once the evaluation is complete so you **can reset or disable the key**. **Do not hard-code API keys in your source code.**
   - **Attachment:** Your prepared `.zip` archive.

### 4. Submission Frequency and Evaluation

- **Submission Frequency:** We allow each team to make **1-2 submissions within a 2-month period**. Each submission can include up to 2 model checkpoints, and you may choose up to 2 of the best results to update on the leaderboard.
- **Evaluation Process:** Your submission will be evaluated once on the main PARROT test set. Based on the results, we will automatically calculate your scores ($Acc_{EX}$ and $Acc_{RES}$) on the **Overall Leaderboard** and all relevant **Single-Dialect Leaderboards**. After the evaluation is complete, we will send you the final scores for confirmation before updating the official leaderboards.

### **IMPORTANT NOTES**

1. **No Reliance on Ground Truth SQL:** Please be aware that in real-world scenarios and in our testing, the ground truth target SQL is **not observable**. Ensure that your method does not rely on this information, as doing so will result in a failed evaluation.
2. **Logging and Error Handling:** **Please ensure your code includes a logging or error-handling mechanism.** This allows us to resume the evaluation from the point of failure after debugging, rather than starting over. This will save significant time and (potentially) API costs. Clear log files also facilitate better communication when issues arise.
    *(If your code must be restarted from the beginning after an error, we may not be responsible for the extra API token costs incurred. Thank you for your understanding!)*

### **Disclaimer**

We commit to using your code for evaluation purposes only and will not disseminate or disclose any details of your code. After the evaluation is completed and the results are confirmed with the model author, we will immediately delete the server instance, including your code, models, and all related files.