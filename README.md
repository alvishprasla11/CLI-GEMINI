# 🌟 Gemini CLI App

Welcome to the **Gemini CLI App**, a simple and powerful command-line tool that interacts with the Gemini API. Follow the steps below to set up and run the application seamlessly!

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/alvishprasla11/CLI-GEMINI.git
cd CLI-GEMINI
```

### 2️⃣ Set Up Environment Variables
Create a new `.env` file in the root directory of the project:

```bash
touch .env
```

Then, obtain an **API Key** from [Gemini](https://gemini.google.com) and add it to your `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 3️⃣ Create a Virtual Environment & Install Dependencies
Set up a virtual environment and install the required dependencies:

```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)

pip install -r requirements.txt  # Install dependencies
```

### 4️⃣ Create an Executable File
Convert your script into an executable so it can be easily run from the CLI:

```bash
pyinstaller --onefile --name gemini-cli gemini.py
```

This will generate an executable file inside the `dist` directory.

### 5️⃣ Run the Application
Navigate to the `dist` folder and run the executable:

```bash
cd dist
./gemini-cli  # Mac/Linux
.gemini-cli.exe  # Windows
```

---

## 🎯 Features
✅ Interacts with the **Gemini API** using your API key  
✅ Supports **environment variable configuration** for security  
✅ Simple **command-line interface** for easy usage  
✅ Packaged as an **executable file** for portability  

---

## 🛠 Troubleshooting

- **Permission denied while running the executable(NEED TO DO THIS IN MAC/LINUX!)?**  
  Try giving it execution permissions:
  ```bash
  chmod +x gemini-cli
  ```

- **Issues with dependencies?**  
  Make sure you are in the virtual environment and try reinstalling:
  ```bash
  pip install --force-reinstall -r requirements.txt
  ```

- **Invalid API key error?**  
  Double-check your `.env` file and ensure you copied the correct key.

---

## 🤝 Contributing
Got ideas or improvements? Feel free to **fork** the repo and submit a **pull request**!

---

## 📜 License
This project is licensed under the **MIT License**.

---

### ⭐ If you find this project useful, consider giving it a star ⭐ on GitHub!

Happy coding! 🚀

