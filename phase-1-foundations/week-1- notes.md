# week 1 notes
I learnt about what happens when a "google.com" is writen in a browser, the different phases it passes through and the three way hand shake that happens in the transport layer

## The tcp model
- Application layer
- Transport layer
- Internet layer
- Link layer

## Aplication layer:
This handles the physical interaction between the user and the internet. e.g: The browser(HTTP, HTML, CSS)

## Transport layer:
This is where the three way handshake happens the syncronise and the acknoledgment
| Browser | Syncronise(SYN) |
|---------|-----------------|
| Server | Acknoledge + Syncronise(ACK + SYN) |
|--------|------------------|
| Browser | Acknoledge(ACK) |

## Internet layer:
This layer is where the url that was sent in the application layer gets an ip address this is where the DNS stays

## Link layer:
This is where the ip gets routed to the server with wifi and routers

## Summary
Basically the when the url is typed in it is first confirmed wether the ip is in the cache DNS if it is not it is converterted to an ip address using the internet layer and the transport layer asks for the html, css and js file assocated with tha ip address the server response and sends them to the browser in packets the transport layer checkes if those packes are complete before assembling them if they are not the transport layer request for it so be sent then displays it when it is complete