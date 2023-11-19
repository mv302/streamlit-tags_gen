import streamlit as st
from tags_generator import TagsGenerator
print("hi")
# Set your OpenAI API key
openai_api_key = "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"

# Initialize the TagsGenerator with custom attributes
tg = TagsGenerator(openai_api_key)

def main():
    st.title("Tags Generator with Streamlit")

    # Input text
    text = st.text_area("Enter text for tag generation", height=200)

    if st.button("Generate Tags"):
        if text:
            # Generate tags
            tags = tg.generate_tags(text)
            st.success("Tags generated successfully!")
            
            # Display the generated tags
            st.subheader("Generated Tags:")
            st.write(tags)
        else:
            st.warning("Please enter some text for tag generation.")

if __name__ == "__main__":
    main()
