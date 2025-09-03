from rag import add_documents

if __name__ == "__main__":
    docs = [
        "Refunds are possible within 30 days of purchase with a receipt.",
        "To reset the device, hold the power button for 10 seconds.",
        "The support email is support@example.com.",
        "The maximum file size allowed is 25 MB.",
        "All products come with a 12-month warranty."
    ]
    add_documents(docs)
    print("Added sample documents.")
