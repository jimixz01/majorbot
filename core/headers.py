def headers(token=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        # "Cookie": "cf_clearance=JqQjVp7WbziVg9sBATf7gWGK.NuEEIjTr4OAyoMiS2Y-1724063187-1.2.1.1-Uw_v63CWY.yaw8obXeP9UxdFXIk9kS5F6hKR1glQbYnKyTKpnFWB7yGGdVVp31VNafsDWWPrzLzJJNv5e9ZBXMhTz8RGnu5DXTGFuxPUBtbverkj9gd3iHoFCVPeMioiGFGFQk09pwTOzO546RMHeX10ryTUSaPdPKs0jfDJX7bxFa0MCyyXq7eoTOn20cEkdsL9Q9_uU5VnZmt9rnYtT3qaHSoSOp0.q2yppyiiReUtmXAc_FOsKNA6poVVVW9WYAEJdTCXLlYhicoRFeM0cHJ781FVnCY2xHZ7tH6OLSArbEC0PFm0XE6RzTRBnsEe6tWfPQ5SQGqW358Py080FS2uh.dB12QlvKLB50vsVQp_txWeqI0blGqZYdY2pak5",
        "Origin": "https://major.glados.app",
        "Referer": "https://major.glados.app/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers
