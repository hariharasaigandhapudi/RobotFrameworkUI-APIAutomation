run_all_in_parallel:
	make -j test_Windows_10_edge_latest test_OX_X_10_11_firefox_latest

test_Windows_10_edge_latest:
	robot  --variable platform:"Windows 10" --variable browserName:MicrosoftEdge Tests/Sources/login.robot

test_OX_X_10_11_firefox_latest:
	robot --variable platform:"macOS Sierra" --variable browserName:firefox Tests/Sources/login.robot