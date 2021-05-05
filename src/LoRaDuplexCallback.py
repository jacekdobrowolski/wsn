import time
import config_lora


msgCount = 0  # count of outgoing messages
INTERVAL = 2000  # interval between sends
INTERVAL_BASE = 2000  # interval between sends base



def duplexCallback(lora):
    print("LoRa Duplex with callback")
    lora.onReceive(on_receive)  # register the receive callback
    do_loop(lora)



def do_loop(lora):
    global msgCount

    lastSendTime = 0
    interval = 0

    while True:
        now = config_lora.millisecond()
        if now < lastSendTime:
            lastSendTime = now

        if (now - lastSendTime > interval):
            lastSendTime = now  # timestamp the message
            interval = (lastSendTime % INTERVAL) + INTERVAL_BASE  # 2-3 seconds

            message = "{} {}".format(config_lora.NODE_NAME, msgCount)
            sendMessage(lora, message)  # send message
            msgCount += 1

            lora.receive()  # go into receive mode



def sendMessage(lora, outgoing):
    lora.println(outgoing)
    # print("Sending message:\n{}\n".format(outgoing))



def on_receive(lora, payload):
    from machine import I2C, Pin
    import ssd1306

    i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    lora.blink_led()

    try:
        payload_string = payload.decode()
        rssi = lora.packetRssi()
        oled.fill(0)
        oled.text("Received message\n", 0, 0)
        oled.text("{}".format(payload_string), 0, 16)
        print("*** Received message ***\n{}".format(payload_string))
        if config_lora.IS_TTGO_LORA_OLED:
            lora.show_packet(payload_string, rssi)
    except Exception as e:
        print(e)
    print("with RSSI {}\n".format(rssi))
    oled.text("with RSSI {}\n".format(rssi), 0, 24)
    oled.show()
