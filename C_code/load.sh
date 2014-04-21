avrdude -b 19200 -P /dev/ttyACM0 -pm32 -c stk500v1 -U flash:w:stepper.hex
