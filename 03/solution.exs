defmodule Day3 do
    def priority(value) do
      if value > 90, do: value - 0x60, else: value - 0x40 + 26
    end

    defp string_to_set(string) do
      MapSet.new(String.to_charlist(string))
    end

    def easy_answer(input) do
      File.stream!(input)
      |> Stream.map(&String.trim/1)
      |> Stream.map(fn line -> String.split_at(line, div(String.length(line),2)) end)
      |> Stream.map(fn pair -> MapSet.intersection(string_to_set(elem(pair, 0)), string_to_set(elem(pair, 1))) end)
      |> Stream.map(&MapSet.to_list/1)
      |> Stream.map(&List.first/1)
      |> Stream.map(&priority/1)
      |> Enum.reduce(&+/2)
    end

    def hard_answer(input) do
      File.stream!(input)
      |> Stream.map(&String.trim/1)
      |> Stream.chunk_every(3)
      |> Stream.map(fn x -> Enum.map(x, &string_to_set/1) end)
      |> Stream.map(fn x -> Enum.reduce(x, &MapSet.intersection/2) end)
      |> Stream.map(fn x -> Enum.take(x, 1) end)
      |> Stream.map(&List.first/1)
      |> Stream.map(&priority/1)
      |> Enum.reduce(&+/2)
    end
end

IO.puts(Day3.easy_answer("input"))
IO.puts("---")
IO.puts(Day3.hard_answer("input"))
