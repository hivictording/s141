from capture.capture_api import CaptureAPI, file_hash

api_client = CaptureAPI(
            "10.7.100.29", "CC41E2C76CF3", "E7C76F3C1383F5C25388E6863C195B44")

file_name = "D://temp//001.jpg"
sha256 = file_hash("sha256", file_name)

# status_code, report = api_client.file_report(sha256, all_info=True)
status_code, data = api_client.file_scan(file_name)

print(status_code)
# print(report)




