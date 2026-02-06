package com.restaurant.orderapi.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.UUID;

@Entity
@Table(name = "order_item")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class OrderItem {
    
    @Id
    @Column(columnDefinition = "UUID")
    private UUID idOrderItem;
    
    @Column(nullable = false, columnDefinition = "UUID")
    private UUID idOrders;
    
    @Column(nullable = false, columnDefinition = "UUID")
    private UUID idProduct;
    
    @Column(nullable = false)
    private Integer quantity;
    
    @Column(length = 255)
    private String note;
}
