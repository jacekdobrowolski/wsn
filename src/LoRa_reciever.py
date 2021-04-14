def receive(lora):
    print("LoRa Receiver")
    display = Display()

    while True:
        if lora.received_packet():
            lora.blink_led()
            print('something here')
            payload = lora.read_payload()
            print(payload)
