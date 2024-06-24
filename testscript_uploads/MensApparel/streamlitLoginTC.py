import streamlit as st
import pandas as pd
import subprocess
def main():
    st.title("Login Test Data Selection")
    uploaded_file = st.file_uploader("Upload your file here...")
    df = pd.read_excel(uploaded_file)
    num_rows=2
    option=[]
    i=1
    j=0
    passval=1
    for index, row in df.head(2).iterrows():
        option.append(st.checkbox("Option "+str(i)+":  "+row["Web_Email"]+"  "+str(row["Web_Password"]), value=False))
        i+=1
    
    selected_options=[]
    if st.button("Submit"):
        # Run the second script with selected options
        i=1
        for x in option:
            if x:
                selected_options.append(i)
            if x<6:
                passval=2
            i+=1
        st.write(selected_options)
        with open("testcaseoptions.txt", "w") as file:
            for z in selected_options:
                file.write(str(df.loc[int(z)-1,'Web_Email'])+" ")
                file.write(str(df.loc[int(z)-1,'Web_Password']))

        subprocess.run(["python", "..\\server\\loginTestScript.py"])
        st.write("hi")
        #command = ['python', 'second_script.py'] + [f'--{key}' for key, value in selected_options.items() if value]
        #st.info(f"Running: {' '.join(command)}")
        #st.text("Output:")
    # Display selected options
    #i=1
    #st.write("Selected Options:")
    #for x in option:
    #    if x:
    #        st.write("- Option ",i,":",x)
    #        passval.append(i)
    #    if x == False:
    #        passval.remove(i)
    #    i+=1    
    #st.write(passval)

if __name__ == "__main__":
    main()
