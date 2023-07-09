from django import dispatch
user_visit_signal = dispatch.Signal(["date_time","ip","device"])
invalid_notice_signal = dispatch.Signal([])
