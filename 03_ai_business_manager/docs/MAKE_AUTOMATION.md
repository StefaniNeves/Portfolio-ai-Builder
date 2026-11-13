# Make automation guide

This is a reproducible implementation guide, not a claim that a Make scenario has already
been created or run in your account.

## Scenario: send sales rows to the API
1. Create a scenario in Make.
2. Add a **Webhooks > Custom webhook** trigger and copy its URL.
3. Add **HTTP > Make a request**.
4. Configure method `POST`, content type `application/json`, and point it to the deployed
   FastAPI `/analyze` endpoint (or a temporary local tunnel during development).
5. Map the incoming `records` array and send `{"records": [...], "use_ai": false}`.
6. Add a router or notification module to send the summary to an approved destination.
7. Test with `examples/request.json`, inspect the run history, and capture your own screenshot.

Keep credentials in Make's connection manager. Do not paste secrets into screenshots or Git.
Record the date, test input, result, and any errors in your project evidence log.
