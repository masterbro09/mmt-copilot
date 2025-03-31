import * as vscode from 'vscode';
import axios from 'axios';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('mmt-copilot.suggestCode', async () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const userInput = await vscode.window.showInputBox({ prompt: "Describe the code you want" });
        if (!userInput) return;

        try {
            const res = await axios.post('http://localhost:8000/generate-code', { prompt: userInput });
            const suggestion = res.data.code;

            editor.edit(editBuilder => {
                const position = editor.selection.active;
                editBuilder.insert(position, "\n" + suggestion);
            });
        } catch (error) {
            vscode.window.showErrorMessage("Error fetching code suggestion");
        }
    });

    context.subscriptions.push(disposable);
}
