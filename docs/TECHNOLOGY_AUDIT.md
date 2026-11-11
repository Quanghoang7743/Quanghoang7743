# Công nghệ đã kiểm tra trên GitHub Quanghoang7743

Ngày kiểm tra: 11/11/2026. Phạm vi: 29 repo công khai tại thời điểm bắt đầu; 25 repo không phải fork. Không suy luận mức độ thành thạo từ dependency hoặc repo fork.

| Nhóm | Công nghệ xác nhận | Bằng chứng |
| --- | --- | --- |
| Web | JavaScript, TypeScript, React, Next.js, Vite, Tailwind CSS, Material UI, Ant Design, Redux Toolkit, Zustand | [Portfolio/package.json](https://github.com/Quanghoang7743/Portfolio/blob/main/package.json), [EmployeeManager/package.json](https://github.com/Quanghoang7743/EmployeeManager/blob/main/package.json), [MusicProject/package.json](https://github.com/Quanghoang7743/MusicProject/blob/main/package.json) |
| Backend | PHP, Laravel, Sanctum, Reverb | [Manager_Saff_Project/composer.json](https://github.com/Quanghoang7743/Manager_Saff_Project/blob/main/composer.json), [CourceManager/composer.json](https://github.com/Quanghoang7743/CourceManager/blob/main/composer.json) |
| Node backend / realtime | Node.js, Express, Socket.IO | [gc/package.json](https://github.com/Quanghoang7743/gc/blob/main/package.json) |
| Flutter mobile | Dart, Flutter, Provider, Pusher; Firebase Auth, Firestore, Storage | [MApp/pubspec.yaml](https://github.com/Quanghoang7743/MApp/blob/main/pubspec.yaml), [Reedmit/pubspec.yaml](https://github.com/Quanghoang7743/Reedmit/blob/main/pubspec.yaml) |
| React Native mobile | React Native, Expo, Expo Router, TypeScript, Zustand | [NiMix/package.json](https://github.com/Quanghoang7743/NiMix/blob/main/package.json) |
| Desktop | Electron, electron-builder | [GameXO/package.json](https://github.com/Quanghoang7743/GameXO/blob/master/package.json) |
| Game scripts | C#, Unity (UnityEngine / MonoBehaviour) | [ScriptGame/Player.cs](https://github.com/Quanghoang7743/ScriptGame/blob/main/Player.cs) |
| Computer vision | Python, OpenCV, PyTorch, torchvision, Ultralytics YOLO, CustomTkinter | [OpenCV_FRUIT_AI/requirements.txt](https://github.com/Quanghoang7743/OpenCV_FRUIT_AI/blob/main/requirements.txt) |
| Data | NumPy, pandas, PyArrow, Pydantic | [Bot_Gold/pyproject.toml](https://github.com/Quanghoang7743/Bot_Gold/blob/main/pyproject.toml) |
| Khai báo tùy chọn | scikit-learn, LightGBM, Streamlit, MetaTrader5 | Extras trong [Bot_Gold/pyproject.toml](https://github.com/Quanghoang7743/Bot_Gold/blob/main/pyproject.toml); không xem là đã triển khai thực tế |

## Các điểm đã loại khỏi suy luận

- `web-bangiay-java` hiện chứa HTML/CSS/JavaScript; chưa có bằng chứng Java trong cây mã đã đọc.
- Nhãn C++ ở `GameMode` có các file runner được Flutter sinh tự động; không dùng nó để khẳng định kinh nghiệm C++.
- Không lấy công nghệ từ 4 repo fork để đưa vào danh sách kỹ năng.
- `BookManager`, `Website_MoxChat`, `hightzone` chưa có cây mã; `ShopShoe`, `KTDHMT` chỉ có README.
- Dependency là bằng chứng công nghệ được khai báo trong dự án, không chứng minh chất lượng, kinh nghiệm hoặc trạng thái triển khai.

## Hồ sơ và cập nhật tự động

Repo hồ sơ là `Quanghoang7743/Quanghoang7743`, nhánh `main`.

- `metrics.yml`: cập nhật hai thẻ SVG từ GitHub public API mỗi ngày; ngôn ngữ tính theo số byte mã trong repo công khai không phải fork, có thể bao gồm mã sinh tự động.
- `contrib.yml`: cập nhật lịch đóng góp 3D mỗi ngày.
- `snake.yml`: cập nhật hoạt ảnh rắn trên nhánh `output` mỗi 12 giờ.
- Cả ba dùng `secrets.GITHUB_TOKEN` do GitHub cấp sẵn, quyền `contents: write`; không cần METRICS_TOKEN hoặc WakaTime.
- Không đưa các ảnh đóng góp cũ của chủ mẫu vào repo hồ sơ mới. Giữ nguồn tham khảo thiết kế: [Johnserf-Seed/Johnserf-Seed](https://github.com/Johnserf-Seed/Johnserf-Seed).
