#include "mh-uart.c"

#define FORWARD 1
#define BACKWARD 2
#define ENABLE 3
#define DISABLE 4
#define STATUS 5

int main(void)
{
uint8_t steps[4];
steps[0]=12;
steps[1]=6;
steps[2]=3;
steps[3]=9;

uint8_t data,pos=0,enabled=0;

uart_init(38400);
DDRC=255;
DDRD=4; //(1<<PD2);
PORTD=0;
PORTC=0;
for(;;)
  {
    data = uart_recv_byte();

	if(enabled){
		if(data==FORWARD){if(pos<3)pos+=1;else{pos=0;} }
		else if(data==BACKWARD){if(pos>0)pos-=1;else{pos=3;} }
		}
	if(data==ENABLE){PORTD=4;PORTC=steps[pos];enabled=1;}
	else if(data==DISABLE){PORTD=0;PORTC=0;enabled=0;}
	else if(data==STATUS){uart_send_byte(steps[pos]);uart_send_byte(enabled);}

    if(enabled)PORTC=steps[pos];
  }
}
