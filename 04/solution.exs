defmodule Day4 do
    def hard_answer(input) do
    File.stream!(input)
    |> Stream.map(&String.trim/1)
    |> Stream.map(fn x -> String.split(x, [",", "-"]) end)
    |> Stream.map(fn x -> Enum.map(x, &String.to_integer/1) end)
    |> Stream.map(fn [x1, y1, x2, y2] -> (x1 <= y2) and (x2 <= y1) end)
    |> Enum.count(fn x -> x end)
  end


  def easy_answer(input) do
    File.stream!(input)
    |> Stream.map(&String.trim/1)
    |> Stream.map(fn x -> String.split(x, [",", "-"]) end)
    |> Stream.map(fn x -> Enum.map(x, &String.to_integer/1) end)
    |> Stream.map(fn [x1, y1, x2, y2] -> (y2 - y1) * (x1 - x2) >= 0 end)
    |> Enum.count(fn x -> x end)
  end
end

IO.puts(Day4.easy_answer("test-input"))
IO.puts(Day4.easy_answer("input"))
IO.puts(Day4.hard_answer("test-input"))
IO.puts(Day4.hard_answer("input"))