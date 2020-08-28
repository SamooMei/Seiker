# Seiker

Scuffed Bot that notifies people of updates on Elsword Babel through E-Mail

## Self-Hosting
1. Clone the bot:
```bash
git clone https://github.com/SamooMei/Seiker
```
2. Navigate into the newly cloned repo
```bash
cd Seiker
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Enter the bot's credentials as Environment Variables
```python
USER = "ENTER BOT LOGIN USERNAME"
PASS = "ENTER BOT LOGIN PASSWORD"
```
5. Enter the emails that will request updates from the bot in the addresses.json files
```json
{
	"goons": ["firstExample@yahoo.com", "secondExample@yahoo.com"]
}
```
6. Run the bot 
```bash
python Seiker.py
```
