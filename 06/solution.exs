defmodule Day06 do
    def easy_answer(input) do
        File.read!(input)
        |> String.graphemes()
        |> Enum.scan([], &scanner/2)
        |> Enum.take_while(fn x -> length(Enum.uniq(x)) < 4 end)
        |> length() |> add_one()
        
    end

    def scanner(element, acc) do
        acc = if length(acc) >= 4, do: List.delete_at(acc, 0), else: acc
        acc ++ [element]
    end

    def hard_scanner(element, acc) do
        acc = if length(acc) >= 14, do: List.delete_at(acc, 0), else: acc
        acc ++ [element]
    end

    def add_one(value) do
        value + 1
    end

    def hard_answer(input) do
        File.read!(input)
        |> String.graphemes()
        |> Enum.scan([], &hard_scanner/2)
        |> Enum.take_while(fn x -> length(Enum.uniq(x)) < 14 end)
        |> length() |> add_one()
    end

end

IO.puts(Day06.easy_answer("test-input"))
IO.puts(Day06.easy_answer("input"))
IO.puts(Day06.hard_answer("test-input"))
IO.puts(Day06.hard_answer("input"))
