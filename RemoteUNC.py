import tkinter as tk
import subprocess

root = tk.Tk()
root.configure(bg="#36454f")
root.title("UNC Assist")
output = tk.StringVar()
output.set("Console: ")
badChars = ["\\n", "\\r", "b'"]

def submit():
        e1 = pcField.get()
        e2 = userName.get()
        e3 = userPass.get()
        r = subprocess.Popen('cmd /c "net use \\\\"' + e1.strip() + "\\c$ /user:" + e2.strip() + " " + e3.strip(),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        out, err = r.communicate()
        out = str(out)
        err = str(err)

        if len(out) > 4:
            for i in badChars:
                out = out.replace(i, "")
            output.set(out)
            subprocess.Popen('explorer "\\\\"' + e1.strip() + "\\c$")
        else:
            for i in badChars:
                err = err.replace(i, "")
            output.set(err)

def remove():
    e1 = pcField.get()
    r = subprocess.Popen('cmd /c "net use /delete \\\\"' + e1.strip() + "\\c$",
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = r.communicate()
    out = str(out)
    err = str(err)

    if len(out) > 4:
        for i in badChars:
            out = out.replace(i, "")
        output.set(out)
    else:
        for i in badChars:
            err = err.replace(i, "")
        output.set(err)

pcL = tk.Label(root, text=" PC Name: ", bg="#36454f", relief="ridge", fg="white", font="bold").grid(row=0)
userL = tk.Label(root, text=" Username: ", bg="#36454f", relief="ridge", fg="white", font="bold").grid(row=1)
passL = tk.Label(root, text=" Password: ", bg="#36454f", relief="ridge", fg="white", font="bold").grid(row=2)
console = tk.Label(root, bg="black", textvariable=output, fg="white").grid(row=4, columnspan=3)

pcField = tk.Entry(root, width=28)
userName = tk.Entry(root, width=28)
userPass = tk.Entry(root, width=28, show="*")

pcField.grid(row=0, column=1)
userName.grid(row=1, column=1)
userPass.grid(row=2, column=1)

tk.Button(root, text="Quit", command=root.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Submit", command=submit).grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=4)
tk.Button(root, text="Remove", command=remove).grid(row=3, column=1, columnspan=2, sticky=tk.E, pady=4)

root.mainloop()
