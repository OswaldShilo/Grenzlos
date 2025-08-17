
# Grenzlos 🌍

Grenzlos is an API that helps you check visa requirements between countries.

## Request Body
```json
{
  "passport": "AFG",
  "destination": "ALB"
}
```

- **passport** → The ISO Alpha-3 code of the passport country (e.g., `AFG` for Afghanistan).
- **destination** → The ISO Alpha-3 code of the destination country (e.g., `ALB` for Albania).

## Response Example
```json
{
  "passport": "AFG",
  "destination": "ALB",
  "visa_required": true,
  "visa_type": "Visa on Arrival",
  "stay_duration": "30 days"
}
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/OswaldShilo/Grenzlos.git
cd Grenzlos
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```

### 5. Test the API
Open browser or use Postman/cURL:

```
http://127.0.0.1:8000/docs
```

## Deployment

### Render (recommended)
1. Push your code to GitHub (Grenzlos repo).
2. Go to [Render](https://render.com).
3. Create a new Web Service.
4. Connect your GitHub repository.
5. Choose environment:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
6. Deploy.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

📧 Credits

Original Creator: @ThekareemOne

Extended by: Grenzlos (Inya.ai Project)

⭐ If you find this useful, please star both repos!

## License
This project is licensed under the MIT License.

```
Copyright (c) 2023 Oswald Shilo
