from discord_webhooks import DiscordWebhooks

webhook_url = "https://discordapp.com/api/webhooks/937197140768329819/abntJ2hraDAPkaQ9hFy48wS9GoUyzUlHxvxP4hq4MxDSIfMcPdfC10kfpGPPAhUsuiNu" # Put the Discord WebHook Url

def send_msg(class_name, status, start_time, end_time):
    webhook = DiscordWebhooks(webhook_url)
    # Attach the footer
    webhook.set_footer(text = '--Attender Bot')

    if status == "joined":
        webhook.set_content(title=f"{class_name} lecture has started",
                    description = ":heart:")
        #Put the Fields
        webhook.add_field(name = "Class", value = class_name)
        webhook.add_field(name = "Status", value = status)
        webhook.add_field(name = "Joined at", value = start_time)
        webhook.add_field(name = "Leaving at", value = end_time)
        
    elif status == "left":
        webhook.set_content(title=f"I left the {class_name} lecture",
                    description = "heart:")
        #Put the Fields
        webhook.add_field(name = "Class", value = class_name)
        webhook.add_field(name = "Status", value = status)
        webhook.add_field(name = "Joined at", value = start_time)
        webhook.add_field(name = "Left at", value = end_time)
        
    elif status == "noclass":
        webhook.set_content(title=f"today their is no class of {class_name}",
                    description = "heart:")
        #Put the Fields
        webhook.add_field(name = "Class", value = class_name)
        webhook.add_field(name = "Status", value = status)
        webhook.add_field(name = "Expected Join at", value = start_time)
        webhook.add_field(name = "Expected Leave at", value = end_time)
    webhook.send()
    print("Message Send")

# if __name__ == "__main__":
#     #send_msg("Machine Learning", "left", "12:00", "01:00")
