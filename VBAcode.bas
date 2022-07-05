Attribute VB_Name = "Module1"
Sub StockTickerData()
    
    Dim lastRow As Long
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    Dim startPrice As Double
    startPrice = 0
    
    Dim endPrice As Double
    endPrice = 0
    
    Dim x As Integer
    x = 2
    
    Dim volCount As LongLong
    volCount = 0
    
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"
    
    
    For i = 2 To lastRow
    
        volCount = volCount + Cells(i, 7).Value
    
        If startPrice = 0 Then
        
        startPrice = Cells(i, 3).Value
        
        End If
    
    
        If (Cells(i, 1).Value) <> (Cells(i + 1, 1).Value) Then
        
        endPrice = Cells(i, 6).Value
        
        Cells(x, 9).Value = Cells(i, 1).Value
        Cells(x, 10).Value = endPrice - startPrice
            
            If (endPrice - startPrice) > 0 Then
                Cells(x, 10).Interior.ColorIndex = 4
            End If
            
            If (endPrice - startPrice) < 0 Then
                Cells(x, 10).Interior.ColorIndex = 3
            End If
            
        
        Cells(x, 11).Value = FormatPercent(Round((((endPrice / startPrice) - 1)), 4))
        Cells(x, 12).Value = volCount
        
        x = x + 1
        
        startPrice = 0
        endPrice = 0
        volCount = 0
        
        End If
    
    
    Next i


    Cells(1, 16).Value = "Ticker"
    Cells(1, 17).Value = "Value"
    Cells(2, 15).Value = "Greatest % Increase"
    Cells(3, 15).Value = "Greatest % Decrease"
    Cells(4, 15).Value = "Greatest Total Volume"
    
    Dim tickerLastRow As Integer
    tickerLastRow = x
    
    Dim greatestIncrease As Variant
    greatestIncrease = Cells(2, 11).Value
    
    Dim greatestIncreaseTicker As String
    greatestIncreaseTicker = Cells(2, 9).Value
    
    Dim greatestDecrease As Variant
    greatestDecrease = Cells(2, 11).Value
    
    Dim greatestDecreaseTicker As String
    greatestDecreaseTicker = Cells(2, 9).Value
    
    Dim greatestVolume As LongLong
    greatestVolume = Cells(2, 12).Value
    
    Dim greatestVolumeTicker As String
    greatestVolumeTicker = Cells(2, 9).Value
    
    For j = 2 To tickerLastRow
    
        If (Cells(j, 11).Value > greatestIncrease) Then
        
            greatestIncrease = Cells(j, 11).Value
            greatestIncreaseTicker = Cells(j, 9).Value
        
        End If
        
        If (Cells(j, 11).Value < greatestDecrease) Then
        
            greatestDecrease = Cells(j, 11).Value
            greatestDecreaseTicker = Cells(j, 9).Value
        
        End If
        
        If (Cells(j, 12).Value > greatestVolume) Then
        
            greatestVolume = Cells(j, 12).Value
            greatestVolumeTicker = Cells(j, 9).Value
        
        End If
    
    Next j


    Cells(2, 17).Value = FormatPercent(greatestIncrease)
    Cells(3, 17).Value = FormatPercent(greatestDecrease)
    Cells(4, 17).Value = greatestVolume
    
    Cells(2, 16).Value = greatestIncreaseTicker
    Cells(3, 16).Value = greatestDecreaseTicker
    Cells(4, 16).Value = greatestVolumeTicker

End Sub
