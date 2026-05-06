`default_nettype none

module tt_um_alu8bit (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);
    reg [7:0] b_reg;
    wire [7:0] a      = ui_in;
    wire [7:0] b      = b_reg;
    wire [2:0] opcode = uio_in[2:0];
    wire       load_b = uio_in[3];

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) b_reg <= 8'h00;
        else if (load_b) b_reg <= ui_in;
    end

    reg [7:0] result;
    reg       zero;

    always @(*) begin
        case(opcode)
            3'b000: result = a + b;
            3'b001: result = a - b;
            3'b010: result = a & b;
            3'b011: result = a | b;
            3'b100: result = a ^ b;
            3'b101: result = ~a;
            3'b110: result = b;
            default: result = 8'h00;
        endcase
        zero = (result == 8'h00);
    end

    assign uo_out  = result;
    assign uio_out = {7'b0, zero};
    assign uio_oe  = 8'hFF;

endmodule
