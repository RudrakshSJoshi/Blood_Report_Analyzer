# Configuration Steps

1. Install [pipx](https://pipx.pypa.io/stable/installation/)
2. Make sure pipx is included in PATH, mentioned in the above link as well.
3. Install poetry
```bash
pipx install poetry
```
4. Create a local repository using git clone
5. Open Project in Terminal and enter the command
```bash
poetry install --no-root
```
6. Copy PATH of your environment by copying the path of virtual environment using the following command in Terminal.
```bash
poetry shell
```
7. Change Interpreter Path to the path copied from above step.
8. To set up LLMs, first install [Ollama](https://ollama.com/) (Skip to Step 15 if you intend to use groq API)
9. After that open terminal and enter the following
```bash
ollama pull llama2
ollama pull mistral
```
10. The above steps will take time and space, which may cause time lag for some time
11. To check whether LLMs are properly installed, write the following command
```bash
ollama list
```
12. The above should give you a list of installed LLMs
13. In case of Windows, open git bash, linux users can just diirectly open terminal and enter the following commands on project folder terminal
```bash
chmod +x ./llm_configure/create-llama2-model-file.sh
./llm_configure/create-llama2-model-file.sh
chmod +x ./llm_configure/create-mistral-model-file.sh
./llm_configure/create-mistral-model-file.sh
```
14. This will allow your LLMs to be compatible with CrewAI.
15. Now in agents.py file, you may change llm(line 35) by changing model to:
a. crewai-mistral
b. crewai-llama2
c. any of groq LLMs (if you are using groq api), such as mixtral-8x7b-32768.
based on your preference (I prefer mistral over llama2)
16. Run main.py file and it should work
