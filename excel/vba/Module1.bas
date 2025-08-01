Attribute VB_Name = "Module1"
Option Explicit

'------------------------------------------------------------
' OptimizeHeadcount
'------------------------------------------------------------
' Sheet "Input":
'   A = size_bucket  |  B = units_scanned  |  C = target_rate
'   D (output) = headcount_needed = CEILING(units / rate)
'------------------------------------------------------------
Sub OptimizeHeadcount()
    Dim ws As Worksheet: Set ws = Sheets("Input")
    Dim lastRow As Long: lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    Dim r As Long, units As Long, rate As Long
    
    For r = 2 To lastRow
        If ws.Cells(r, "A").Value = "" Then Exit For
        units = ws.Cells(r, "B").Value
        rate  = ws.Cells(r, "C").Value
        ws.Cells(r, "D").Value = Application.Ceiling(units / rate, 1)
    Next r
    
    MsgBox "Head-count calculation complete!", vbInformation
End Sub

