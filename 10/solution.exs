defmodule Day10 do
  def do_operation("noop", {tick, ending_value}) do
    {[{tick + 1, ending_value}], {tick + 1, ending_value}}
  end

  def do_operation(string, {tick, ending_value}) do
    ["addx", number] = String.split(string)
    {[{tick + 1, ending_value}, {tick + 2, ending_value}], {tick + 2, ending_value + String.to_integer(number)}}
  end


  def easy_answer(input) do
    File.stream!(input)
    |> Stream.map(&String.trim/1)
    |> Stream.transform({0,1}, &do_operation/2)
    |> Stream.filter(fn {tick, _} -> rem(tick, 40) == 20 end)
    |> Stream.map(fn {tick, value} -> tick * value end)
    |> Enum.reduce(&+/2)
  end

    def hard_answer(input) do
    File.stream!(input)
    |> Stream.map(&String.trim/1)
    |> Stream.transform({0,1}, &do_operation/2)
    |> Stream.map(fn {tick, value} -> if(abs(rem(tick, 40) - value - 1) < 2, do: "#", else: ".") end)
    |> Stream.chunk_every(40)
    |> Stream.map(fn x -> Enum.reduce(x, &(&2 <> &1)) end)
    |> Stream.each(&IO.puts/1)
    |> Stream.run()
  end

end

IO.puts(Day10.easy_answer("test-input"))
IO.puts(Day10.easy_answer("input"))
Day10.hard_answer("test-input")
IO.puts("")
Day10.hard_answer("input")